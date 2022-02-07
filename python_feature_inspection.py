"""
Section 1
Multithreading - Difference between Process And Thread
Keyword - Process, Thread
"""

"""
(1).프로세스
    - 운영체제 -> 할당 받는 자원 단위(실행 중인 프로그램)
    - CPU동작 시간, 주소공간(독립적)
    - Code, Data, Stack, Heap -> 독립적
    - 최소 1개의 메인스레드 보유 (프로세스 내부에 스레드가 존재)
    - 파이프, 파일, 소켓등을 사용해서 프로세스간 통신(Cost 높음)-> Context Switching

(2).스레드
    - 프로세스 내에 실행 흐름 단위
    - 프로세스 자원 사용
    - Stack만 별도 할당 나머지는 공유(Code, Data, Heap)
    - 메모리 공유(변수 공유)
    - 한 스레드의 결과가 다른 스레드에 영향 끼침
    - 동기화 문제는 정말 주의(디버깅 어려움)

(3).멀티 스레드
    - 한 개의 단일 어플리케이션(응용프로그램) -> 여러 스레드로 구성 후 작업 처리
    - 시스템 자원 소모 감소(효율성), 처리량 증가(Cost 감소)
    - 통신 부담 감소, 디버깅 어려움, 단일 프로세스에는 효과 미약, 자원 공유 문제(교착상태), 프로세스 영향준다.

(4).멀티 프로세스
    - 한 개의 단일 어플리케이션(응용프로그램) -> 여러 프로세스로 구성 후 작업 처리
    - 한 개의 프로세스 문제 발생은 확산 없음(프로세스 Kill)
    - 캐시 체인지, Cost 비용 매우 높음(오버헤드), 복잡한 통신 방식 사용
"""

"""
Section 1
Multithreading - Thread(1) - Basic
Keyword - threading basic
"""
import logging
import threading
import time

# 스레드 실행 함수
def thread_func(name):
    logging.info("Sub-Thread %s: starting", name)
    time.sleep(3)
    logging.info("Sub-Thread %s: finishing", name)

# 메인 영역
if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread : before creating thread")
    
    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First',))

    logging.info("Main-Thread : before running thread")
   
    # 서브 스레드 시작
    x.start()

    logging.info("Main-Thread : wait for the thread to finish")
    
    # 주석 전후 결과 확인
    # x.join()
    
    logging.info("Main-Thread : all done")