def classify_consulting(processed_query):
    """
    컨설팅 관련 쿼리인지 분류하는 함수
    
    Args:
        processed_query (dict): {
            'user_query': str,
            'analyzed_query': Any,
            'action_logs': str
        }
    
    Returns:
        dict: {
            'is_consulting': bool,      # 컨설팅 관련 여부
            'confidence': float,        # 신뢰도 (0.0 ~ 1.0)
            'consulting_type': str,     # 컨설팅 유형 (예: 'business', 'technical', 'design' 등)
            'required_info': list,      # 필요한 추가 정보
            'action_logs': str          # 로그
        }
    """
    # TODO: 실제 컨설팅 분류 로직 구현
    return {
        'is_consulting': False,
        'confidence': 0.0,
        'consulting_type': None,
        'required_info': [],
        'action_logs': processed_query.get('action_logs', '')
    }

def classify_qa(processed_query):
    """
    QA 관련 쿼리인지 분류하는 함수
    
    Args:
        processed_query (dict): {
            'user_query': str,
            'analyzed_query': Any,
            'action_logs': str
        }
    
    Returns:
        dict: {
            'is_qa': bool,             # QA 관련 여부
            'confidence': float,        # 신뢰도 (0.0 ~ 1.0)
            'qa_type': str,            # QA 유형 (예: 'technical', 'usage', 'feature' 등)
            'related_docs': list,       # 관련 문서 목록
            'action_logs': str          # 로그
        }
    """
    # TODO: 실제 QA 분류 로직 구현
    return {
        'is_qa': False,
        'confidence': 0.0,
        'qa_type': None,
        'related_docs': [],
        'action_logs': processed_query.get('action_logs', '')
    }

def classify_human(processed_query):
    """
    인간 상담이 필요한 쿼리인지 분류하는 함수
    
    Args:
        processed_query (dict): {
            'user_query': str,
            'analyzed_query': Any,
            'action_logs': str
        }
    
    Returns:
        dict: {
            'needs_human': bool,        # 인간 상담 필요 여부
            'confidence': float,        # 신뢰도 (0.0 ~ 1.0)
            'urgency_level': str,       # 긴급도 ('low', 'medium', 'high')
            'reason': str,              # 인간 상담이 필요한 이유
            'action_logs': str          # 로그
        }
    """
    # TODO: 실제 인간 상담 필요 여부 분류 로직 구현
    return {
        'needs_human': False,
        'confidence': 0.0,
        'urgency_level': 'low',
        'reason': None,
        'action_logs': processed_query.get('action_logs', '')
    } 