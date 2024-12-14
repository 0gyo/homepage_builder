from pydantic import BaseModel

from gpt_client import GPTClientMain, GPTClientOutput
from prompts import *


async def analyze_humanity_query(processed_query):
    """
    인간스러운 답변이 필요한 쿼리인지 분석하는 함수

    Args:
        processed_query: 처리된 쿼리 데이터

    Returns:
        analysis_result: 인간 답변 필요 여부 분석 결과
    """


async def print_humanity_result(analysis_result):
    """
    인간 답변 필요 여부 분석 결과를 출력하는 함수

    Args:
        analysis_result: 인간 답변 필요 여부 분석 결과

    Returns:
        output_result: 인간 답변 필요 여부 출력 결과
    """


async def analyze_humanity_response(output_result):
    """
    인간스러운 답변을 분석하는 함수

    Args:
        output_result: 인간 답변 필요 여부 출력 결과

    Returns:
        analysis_result: 인간스러운 답변 분석 결과
    """


async def print_humanity_response(analysis_result):
    """
    인간스러운 답변 분석 결과를 출력하는 함수

    Args:
        analysis_result: 인간스러운 답변 분석 결과

    Returns:
        output_result: 인간스러운 답변 출력 결과
    """


async def process_humanity(query_result):
    """
    인간스러운 답변 단계를 수행하는 함수
    """

    humanity_analysis = await analyze_humanity_query(query_result)
    humanity_output = await print_humanity_result(humanity_analysis)

    humanity_response_analysis = await analyze_humanity_response(humanity_output)
    humanity_response_output = await print_humanity_response(humanity_response_analysis)

    return humanity_response_output
