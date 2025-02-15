from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def get_emails(start_id):
            stack = [start_id]
            emails = set()
            account_name = accounts[start_id][0]

            while stack:
                acc_id = stack.pop()

                if acc_id in visited:
                    continue

                visited.add(acc_id)
                
                for idx in range(1, len(accounts[acc_id])):
                    emails.add(accounts[acc_id][idx])

                for nxt in graph[acc_id]:
                    stack.append(nxt)

            return [account_name] + sorted(list(emails))


        graph = {account_id: [] for account_id in range(len(accounts))}
        email_account_id = {}

        for account_id, account in enumerate(accounts):
            for idx in range(1, len(account)):
                email = account[idx]
                
                if email in email_account_id:
                    graph[email_account_id[email]].append(account_id)
                    graph[account_id].append(email_account_id[email])
                else:
                    email_account_id[email] = account_id

        ans = []
        visited = set()

        for account_id in graph:
            if account_id not in visited:
                ans.append(get_emails(account_id))

        return ans