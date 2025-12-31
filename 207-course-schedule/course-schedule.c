bool canFinish(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize) {
    int* indegree = (int*)calloc(numCourses, sizeof(int));

    for (int i = 0; i < prerequisitesSize; i++) {
        int course = prerequisites[i][0];
        indegree[course]++;
    }
    int* queue = (int*)malloc(numCourses * sizeof(int));
    int front = 0, rear = 0;
    for (int i = 0; i < numCourses; i++) {
        if (indegree[i] == 0) {
            queue[rear++] = i;
        }
    }

    int completed = 0;

    while (front < rear) {
        int curr = queue[front++];
        completed++;

        for (int i = 0; i < prerequisitesSize; i++) {
            if (prerequisites[i][1] == curr) {
                int next = prerequisites[i][0];
                indegree[next]--;
                if (indegree[next] == 0) {
                    queue[rear++] = next;
                }
            }
        }
    }
    free(indegree);
    free(queue);
    return completed == numCourses;
}
