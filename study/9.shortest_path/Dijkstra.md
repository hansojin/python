## 다익스트라 최단 경로 알고리즘

* 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산한다
* 다익스트라 최단 경로 알고리즘은 **음의 간선이 없을 때 정상적으로 동작** 한다
    * 현실 세계의 도로(간선)은 음의 간선으로 표현되지 않습니다
* 다익스트라 최단 경로 알고리즘은 **그리디 알고리즘으로 분류** 된다
    * 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복한다

--- 

### 동작 과정

1. 출발 노드를 설정한다
2. 최단 거리 테이블을 초기화한다
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다
5. 위 과정에서 3번과 4번을 반복한다

--- 

### 다익스트라 알고리즘의 특징

* 그리디 알고리즘
    * 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복한다
* 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않는다
    *  한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있다
* 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장된다
    *  완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어야 한다

### 간단한 다익스트라 알고리즘 구현 

* 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 테이블의 모든 원소를 확인(순차 탐색)한다
    * 성능 분석
        * 총 O(V) 번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 한다
        * 전체 시간 복잡도는 O(V²) 
        * 일반적으로 코딩 테스트의 최단 경로 문제에서 전체 노드의 개수가 5,000개 이하라면 이 코드로 문제를 해결할 수 있다
        * 하지만 노드의 개수가 10,000개를 넘어가는 문제라면 어떻게 해야 할까?

--- 

### 우선순위 큐(Priority Queue)

* 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조이다
* 예를 들어 여러 개의 물건 데이터를 자료구조에 넣었다가 높은 물건 데이터부터 꺼내서 확인해야하는 경우에 우선순위 큐를 이용할 수 있다
* Python, C++, Java를 포함한 대부분의 프로그래밍 언어에서 표준 라이브러리 형태로 지원한다

| 자료구조 | 추출되는 데이터|
| ------ | ----------- |
| 스택(Stack)	|가장 나중에 삽입된 데이터|
|큐(Queue)	|가장 먼저 삽입된 데이터|
|우선순위 큐(Priority Queue)	|가장 우선순위가 높은 데이터|

### 힙(Heap)

* 우선순위 큐(Priority Queue)를 구현하기 위해 사용하는 자료구조 중 하나이다
* 최소 힙(Min Heap) 과 최대 힙(Max Heap) 이 있다
* 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용된다

| 우선순위 큐 구현 방식	|삽입 시간	|삭제 시간|
| ------ | ----------- |----------- |
|리스트	|O(1)	|O(N)
|힙(Heap)	|O(logN)	|O(logN)

---

## 개선된 다익스트라 알고리즘 구현 방법

* 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 **힙(Heap) 자료구조** 를 이용한다
* 다익스트라 알고리즘이 동작하는 기본 원리는 동일하다
    * 현재 가장 가까운 노드를 저장해 놓기 위해서 힙 자료구조를 추가적으로 이용한다는 점이 다르다
    * 현재의 최단 거리가 **가장 짧은 노드를 선택** 해야 하므로 **최소 힙을 사용** 한다
* 성능분석
    * 시간 복잡도는 O(ElogV)
    * 노드를 하나씩 꺼내 검사하는 반복문(while문)은 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총횟수는 최대 간선의 수(E)만큼 연산이 수행

---

## 플로이드 워셜 알고리즘 개요

* 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산한다
* 플로이드 워셜(Floyd-Warshall) 알고리즘은 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘을 수행한다
     * 다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않다
* 플로이드 워셜은 **2차원 테이블에 최단 거리 정보를 저장한다**
* 플로이드 워셜 알고리즘은 **다이나믹 프로그래밍 유형에 속한다**
* 각 단계마다 특정한 노드 𝑘를 거쳐 가는 경우를 확인한다
    * 𝑎에서 𝑏로 가는 최단 거리보다 𝑎에서 𝑘를 거쳐 𝑏로 가는 거리가 더 짧은지 검사한다
* 점화식 : **D_ab = min(D_ab, D_ak + D_kb)**
* 성능 분석
    * 노드의 개수가 𝑁개일 때 알고리즘상으로 𝑁번의 단계를 수행
        * 각 단계마다 O(N²) 의 연산을 통해 현재 노드를 거쳐 가는 모든 경로를 고려
    * 따라서 플로이드 워셜 알고리즘의 총 시간 복잡도는 O(N³) 

---

