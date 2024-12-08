import json
from database import get_conversation_data, get_action_logs
from query_analyzer import analyze_query
from query_processor import process_query_result
from classifiers import classify_consulting, classify_qa, classify_human
from validators import validate_consulting_result, validate_qa_result

async def lambda_handler(event, context):
    try:
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
        
        # 쿼리 분석 및 처리
        analyzed_query = analyze_query(enriched_query)
        processed_query = process_query_result(analyzed_query)
        
        # 분류 수행 및 검증
        consulting_result = classify_consulting(processed_query)
        consulting_result = validate_consulting_result(consulting_result, processed_query)
        
        qa_result = classify_qa(processed_query)
        qa_result = validate_qa_result(qa_result, processed_query)
        
        human_result = classify_human(processed_query)
        
        # 결과 반환
        return {
            'statusCode': 200,
            'body': json.dumps({
                'analyzed_query': analyzed_query,
                'processed_query': processed_query,
                'classifications': {
                    'consulting': consulting_result,
                    'qa': qa_result,
                    'human': human_result
                }
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }