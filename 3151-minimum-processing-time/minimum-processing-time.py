class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        sorted_tasks = sorted(tasks,reverse=True)
        sorted_processorTime = sorted(processorTime)
        list_processor_time = set()

        for idx in range(len(processorTime)):
            p_tasks = sorted_tasks[idx*4:idx*4+4]
   
            max_p_time = max(p_tasks) +  sorted_processorTime[idx]
            list_processor_time.add(max_p_time)


        return max(list_processor_time)