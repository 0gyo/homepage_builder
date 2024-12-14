from pydantic import BaseModel
from typing import Optional

from gpt_client import GPTClientMain, GPTClientOutput
from prompts import *
from prompts import (
    common_knowledge_prompts,
    information_prompts,
    query_instruction_prompts,
)


system1_prompts = common_knowledge_prompts

messages = [
    {"role": "system", "content": system1_prompts},
]


class ResponseFormat(BaseModel):
    user_name: Optional[str] = None
    user_query: Optional[str] = None
    gpt_response: Optional[str] = None
    action_log: Optional[str] = None


def analyze_user_query(api_key, model, enriched_query):
    """
    사용자 쿼리를 분석하는 함수

    Args:
        enriched_query: 사용자 쿼리를 확장한 데이터
    Returns:
        analysis_result: 쿼리 분석 결과
    """
    system2_prompts = information_prompts.consulting_information_prompts

    user_prompts = query_instruction_prompts.analyze_user_query_prompts

    user_prompts += f"\n\n{enriched_query['user_query']}"

    messages.append = (
        [
            {"role": "system", "content": system2_prompts},
            {"role": "user", "content": user_prompts},
        ],
    )
    response = ResponseFormat(user_name=user_name, action_log=action_log)

    gpt_client = GPTClientMain(api_key, model)
    response = gpt_client.call_gpt(
        messages=messages,
        response_format=ResponseFormat(user_name=user_name, action_log=action_log),
    )

    return response


def print_user_query_result(analysis_result):
    """
    쿼리 분석 결과를 출력하는 함수

    Args:
        analysis_result: 쿼리 분석 결과

    Returns:
        output_result: 쿼리 출력 결과
    """


def process_query(enriched_query):
    """
    쿼리 단계를 수행하는 함수
    """

    analysis_result = analyze_user_query(enriched_query)
    process_result = print_user_query_result(analysis_result)
    return process_result
