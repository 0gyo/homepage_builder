import json
import asyncio
from database import get_conversation_data, get_action_logs
from query_base import process_query
from consulting_base import process_consulting
from qa_base import process_qa
from humanity_base import process_humanity
from process_manager import process_manager

async def process_all_flows(query_process_result):
    """모든 Flow를 처리하는 함수"""
    # 병렬 처리 프로세스
    consulting_process_result = asyncio.create_task(process_consulting(query_process_result))
    qa_process_result = asyncio.create_task(process_qa(query_process_result))
    humanity_process_result = asyncio.create_task(process_humanity(query_process_result))

    # 모든 생성 작업 완료 대기
    pending_tasks = [
        consulting_process_result,
        qa_process_result,
        humanity_process_result
    ]
    
    return await asyncio.gather(*pending_tasks)

async def lambda_handler(event, context):
    try:
        # 사용자 쿼리 및 ID 검증
        user_query = event.get('user_query')
        user_id = event.get('user_id')
        
        if not user_query or not user_id:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'error': 'Both user_query and user_id are required'
                })
            }

        # 데이터베이스에서 컨텍스트 데이터 로드
        conversation_data = get_conversation_data()
        action_logs = get_action_logs()
        enriched_query = {
            'user_query': user_query,
            'conversation_history': conversation_data,
            'action_logs': action_logs
        }
        
        # 쿼리 프로세스
        query_process_result = process_query(enriched_query)
        
        # ProcessManager를 통해 새로운 프로세스 시작
        # 이전 프로세스가 있다면 자동으로 취소됨
        task = await process_manager.start_new_process(
            user_id,
            process_all_flows(query_process_result)
        )
        
        try:
            final_response = await task
        except asyncio.CancelledError:
            return {
                'statusCode': 202,  # Accepted
                'body': json.dumps({
                    'message': 'Previous process was cancelled, new request accepted'
                })
            }

        return {
            'statusCode': 200,
            'body': json.dumps({
                'response': final_response
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }