import os
from supabase import create_client
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# Supabase 클라이언트 초기화
supabase = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_KEY')
)

def get_conversation_data():
    """
    대화 기록을 가져오는 함수
    
    Returns:
        list: 대화 기록 데이터
    """
    try:
        # TODO: 실제 테이블 이름과 쿼리 로직 구현 필요
        response = supabase.table('conversations').select('*').execute()
        return response.data
    except Exception as e:
        print(f"Error fetching conversation data: {str(e)}")
        return []

def get_action_logs():
    """
    사용자 액션 로그를 가져오는 함수
    
    Returns:
        list: 액션 로그 데이터
    """
    try:
        # TODO: 실제 테이블 이름과 쿼리 로직 구현 필요
        response = supabase.table('action_logs').select('*').execute()
        return response.data
    except Exception as e:
        print(f"Error fetching action logs: {str(e)}")
        return [] 