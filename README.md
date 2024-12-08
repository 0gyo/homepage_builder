# Query Analysis Lambda Function

AWS Lambda를 사용한 사용자 쿼리 분석 함수입니다.

## 요구사항

- Python 3.10
- x86 아키텍처 지원 패키지

## 설치 방법

1. 필요한 패키지 설치:
```bash
pip3 install -r requirements.txt
```

2. 환경 변수 설정:
`.env` 파일을 생성하고 다음 변수들을 설정하세요:
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

## 파일 구조

- `lambda_function.py`: 메인 Lambda 함수
- `database.py`: Supabase 데이터베이스 연결 및 쿼리
- `query_analyzer.py`: 사용자 쿼리 분석 로직
- `requirements.txt`: 필요한 패키지 목록

## Lambda 함수 입력 형식

```json
{
    "user_query": "사용자 입력 문자열"
}
```

## Lambda 함수 출력 형식

```json
{
    "statusCode": 200,
    "body": {
        "analysis": {
            "query": "원본 쿼리",
            "analysis_result": "분석 결과"
        }
    }
}
``` 