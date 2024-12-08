import json
import asyncio
from database import get_conversation_data, get_action_logs
from query_base import process_query
from consulting_base import process_consulting
from qa_base import process_qa
from humanity_base import process_humanity

async def lambda_handler(event, context):
    try:
        # 사용자 쿼리 로드
        user_query = event.get('user_query')
        if not user_query:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'User query is required'})
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
        
        # 병렬 처리 프로세스
        ## 컨설팅 프로세스
        consulting_process_result = asyncio.create_task(process_consulting(query_process_result))
        ## qa 프로세스
        qa_process_result = asyncio.create_task(process_qa(query_process_result))
        ## 인간적인 답변 프로세스
        humanity_process_result = asyncio.create_task(process_humanity(query_process_result))

        # 모든 생성 작업 완료 대기
        pending_tasks = [task for task in [
            consulting_process_result,
            qa_process_result,
            humanity_process_result
        ] if task is not None]
        
        generated_response = await asyncio.gather(*pending_tasks) if pending_tasks else []
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'response': generated_response
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }