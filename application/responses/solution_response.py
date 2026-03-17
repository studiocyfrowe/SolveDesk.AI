class SolutionResponse():
    def __init__(self):
        pass

    def retrieve_solutions(query: str, results):
        response = {
            "query": query,
            "solutions": [
                {
                    "issue_id": results['metadatas'][0][i]['issueItemId'],
                    "issue_name": results['metadatas'][0][i]['issueName'],
                    "issue_sympthoms": results['metadatas'][0][i]['issueSympthoms'],
                    "issue_solution": results['metadatas'][0][i]['issueSolution'],
                    "score": round(1 - results['distances'][0][i], 3)
                }
                for i in range(len(results['ids'][0]))
                if (1 - results['distances'][0][i]) > 0.730
            ]
        }

        return response