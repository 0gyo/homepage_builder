from typing import Dict, Optional
import asyncio
from datetime import datetime

class ProcessManager:
    def __init__(self):
        self._active_tasks: Dict[str, asyncio.Task] = {}
        self._last_update: Dict[str, datetime] = {}
    
    async def start_new_process(self, user_id: str, process_coroutine) -> asyncio.Task:
        """
        새로운 프로세스를 시작하고 이전 프로세스가 있다면 취소
        
        Args:
            user_id: 사용자 식별자
            process_coroutine: 실행할 코루틴
            
        Returns:
            asyncio.Task: 생성된 새 태스크
        """
        # 이전 태스크가 있다면 취소
        await self.cancel_user_process(user_id)
        
        # 새 태스크 생성 및 등록
        task = asyncio.create_task(process_coroutine)
        self._active_tasks[user_id] = task
        self._last_update[user_id] = datetime.now()
        
        return task
    
    async def cancel_user_process(self, user_id: str) -> None:
        """
        사용자의 진행 중인 프로세스를 취소
        
        Args:
            user_id: 사용자 식별자
        """
        if user_id in self._active_tasks:
            task = self._active_tasks[user_id]
            if not task.done():
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass  # 정상적인 취소
                except Exception as e:
                    print(f"Error cancelling task for user {user_id}: {str(e)}")
            
            del self._active_tasks[user_id]
            del self._last_update[user_id]
    
    def get_user_task(self, user_id: str) -> Optional[asyncio.Task]:
        """
        사용자의 현재 실행 중인 태스크 조회
        
        Args:
            user_id: 사용자 식별자
            
        Returns:
            Optional[asyncio.Task]: 실행 중인 태스크 또는 None
        """
        return self._active_tasks.get(user_id)
    
    def is_user_processing(self, user_id: str) -> bool:
        """
        사용자의 프로세스 진행 중 여부 확인
        
        Args:
            user_id: 사용자 식별자
            
        Returns:
            bool: 프로세스 진행 중 여부
        """
        task = self.get_user_task(user_id)
        return task is not None and not task.done()

# 전역 ProcessManager 인스턴스
process_manager = ProcessManager() 