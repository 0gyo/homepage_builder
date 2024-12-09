import asyncio

async def analyze_consulting_query(query_process_result):
    """
    컨설팅 관련 쿼리인지 판단하는 함수
    
    Args:
        query_process_result: 쿼리 프로세스 결과
        
    Returns:
        analysis_result: 컨설팅 쿼리 분석 결과
    """

async def print_consulting_result(analysis_result):
    """
    컨설팅 분석 결과를 출력하는 함수
    
    Args:
        analysis_result: 컨설팅 쿼리 분석 결과
        
    Returns:
        output_result: 컨설팅 출력 결과
    """

async def analyze_consulting_validation(output_result):
    """
    컨설팅 관련 쿼리인지 판단한 결과를 분석하는 함수
    
    Args:
        output_result: 컨설팅 출력 결과
        
    Returns:
        analysis_result: 컨설팅 검증 분석 결과
    """

async def print_consulting_validation(analysis_result):
    """
    컨설팅 검증 분석 결과를 출력하는 함수
    
    Args:
        analysis_result: 컨설팅 검증 분석 결과
        
    Returns:
        output_result: 검증된 컨설팅 출력 결과
    """

async def analyze_consulting_action(validated_outp):
    """
    컨설팅 행동 분석하는 함수
    
    Args:
        validated_outp: 검증된 컨설팅 출력 결과
        
    Returns:
        analysis_result: 컨설팅 행동 분석 결과
    """

async def print_consulting_action(analysis_result):
    """
    컨설팅 행동 분석 결과를 출력하는 함수
    
    Args:
        analysis_result: 컨설팅 행동 분석 결과
        
    Returns:
        output_result: 컨설팅 행동 출력 결과
    """

async def analyze_file_data(action_output):
    """
    파일 데이터 분석하는 함수
    
    Args:
        action_output: 사용자 쿼리를 확장한 데이터
        
    Returns:
        file_analysis: 파일 데이터 분석 결과
    """

async def get_design_templates(action_output):
    """
    디자인 템플릿 조회하는 함수
    
    Args:
        action_output: 사용자 쿼리를 확장한 데이터
        
    Returns:
        design_templates: 디자인 템플릿 조회 결과
    """

async def create_final_plan_sheets(action_output):
    """
    최종 기획서 생성하는 함수
    
    Args:
        action_output: 사용자 쿼리를 확장한 데이터
        
    Returns:
        final_plan: 최종 계획서 생성 결과
    """

async def analyze_consulting_response(function_result):
    """
    컨설팅 답변을 분석하는 함수
    
    Args:
        action_output: 컨설팅 행동 출력 결과
        
    Returns:
        analysis_result: 컨설팅 답변 분석 결과
    """

async def print_consulting_response(analysis_result):
    """
    컨설팅 답변 분석 결과를 출력하는 함수
    
    Args:
        response_analysis: 컨설팅 답변 분석 결과
        
    Returns:
        output_result: 컨설팅 답변 출력 결과 
    """

async def process_consulting(query_result):
    """
    컨설팅 단계를 수행하는 함수
    """

    consulting_analysis = await analyze_consulting_query(query_result)
    consulting_output = await print_consulting_result(consulting_analysis)

    validation_analysis = await analyze_consulting_validation(consulting_output)
    validated_output = await print_consulting_validation(validation_analysis)

    action_analysis = await analyze_consulting_action(validated_output)
    action_output = await print_consulting_action(action_analysis)

    action_tasks = [
            asyncio.create_task(analyze_file_data(action_output)),
            asyncio.create_task(get_design_templates(action_output)), 
            asyncio.create_task(create_final_plan_sheets(action_output))
    ]
    function_result = await asyncio.gather(*action_tasks)

    response_analysis = await analyze_consulting_response(function_result)
    response_output = await print_consulting_response(response_analysis)

    return response_output