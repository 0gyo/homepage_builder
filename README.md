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

## 파로젝트 구조

### 메인 파일
- `lambda_function.py`: Lambda 핸들러 (진입점)
- `query_base.py`: 쿼리 처리 기본 템플릿
- `database.py`: Supabase 데이터베이스 연동

### 프로세스 파일
- `consulting_base.py`: 컨설팅 관련 처리
- `qa_base.py`: QA 관련 처리
- `humanity_base.py`: 인간적인 답변 처리

### 설정 파일
- `requirements.txt`: 의존성 패키지 목록
- `.env`: 환경 변수 설정

## 처리 프로세스

각 프로세스는 다음 3단계로 구성됩니다:

1. **분석 (analyze)**
   - 입력 데이터 분석
   - 의도 및 컨텍스트 파악

2. **출력 생성 (print)**
   - 분석 결과를 기반으로 출력 형식 생성
   - 응답 데이터 구조화

3. **전체 실행 (process)**
   - 분석과 출력을 연결
   - 전체 프로세스 관리

## 병렬 처리

Lambda 함수는 세 가지 프로세스를 병렬로 실행합니다:
- 컨설팅 프로세스
- QA 프로세스
- 인간적인 답변 프로세스

## 데이터베이스

Supabase를 사용하여 다음 데이터를 관리합니다:
- 대화 기록 (conversations)
- 액션 로그 (action_logs)