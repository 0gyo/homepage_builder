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

## 프로젝트 구조

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

## 자동 배포

이 프로젝트는 GitHub Actions를 통해 AWS Lambda에 자동으로 배포됩니다.

### 배포 설정

1. **GitHub Secrets 설정**
   - `AWS_ACCESS_KEY_ID`: AWS IAM 액세스 키
   - `AWS_SECRET_ACCESS_KEY`: AWS IAM 시크릿 키
   - `SUPABASE_URL`: Supabase 프로젝트 URL
   - `SUPABASE_KEY`: Supabase 키

2. **AWS Lambda 함수 설정**
   - 함수 이름: `query-analysis-function`
   - 런타임: Python 3.10
   - 핸들러: `lambda_function.lambda_handler`
   - 메모리: 최소 256MB
   - 타임아웃: 최소 30초

### 배포 프로세스

1. main 브랜치에 코드를 push
2. GitHub Actions 자동 실행
3. 테스트 실행
4. 배포 패키지 생성
5. AWS Lambda에 배포

### 배포 상태 확인

GitHub 레포지토리의 Actions 탭에서 배포 상태를 확인할 수 있습니다.