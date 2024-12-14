from pydantic import BaseModel

from gpt_client import GPTClientMain, GPTClientOutput
from prompts import *


async def analyze_qa_query(processed_query):
    """
    QA 관련 쿼리인지 판단하는 함수

    Args:
        processed_query: 처리된 쿼리 데이터

    Returns:
        analysis_result: QA 쿼리 분석 결과
    """


async def print_qa_result(analysis_result):
    """
    QA 분석 결과를 출력하는 함수

    Args:
        analysis_result: QA 쿼리 분석 결과

    Returns:
        output_result: QA 출력 결과
    """


async def analyze_qa_validation(output_result):
    """
    QA 관련 쿼리인지 판단한 결과를 분석하는 함수

    Args:
        output_result: QA 출력 결과

    Returns:
        analysis_result: QA 검증 분석 결과
    """


async def print_qa_validation(analysis_result):
    """
    QA 검증 분석 결과를 출력하는 함수

    Args:
        analysis_result: QA 검증 분석 결과

    Returns:
        output_result: 검증된 QA 출력 결과
    """


async def analyze_qa_response(validated_output):
    """
    QA 답변을 분석하는 함수

    Args:
        validated_output: 검증된 QA 출력 결과

    Returns:
        analysis_result: QA 답변 분석 결과
    """


async def print_qa_response(analysis_result):
    """
    QA 답변 분석 결과를 출력하는 함수

    Args:
        analysis_result: QA 답변 분석 결과

    Returns:
        output_result: QA 답변 출력 결과
    """


async def process_qa(query_result):
    """
    QA 단계를 수행하는 함수
    """

    qa_analysis = await analyze_qa_query(query_result)
    qa_output = await print_qa_result(qa_analysis)

    validation_analysis = await analyze_qa_validation(qa_output)
    validated_output = await print_qa_validation(validation_analysis)

    response_analysis = await analyze_qa_response(validated_output)
    response_output = await print_qa_response(response_analysis)

    return response_output
