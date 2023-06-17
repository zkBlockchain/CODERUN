import requests
import xml.etree.ElementTree as ET


def main():
    contest_name = input()

    members_url = f"http://127.0.0.1:7777/view/participants?contest={contest_name}"
    members_response = requests.get(members_url)
    members_xml = members_response.text

    members_root = ET.fromstring(members_xml)
    members = [member.get('login') for member in members_root.findall('participant')]

    scores = {}

    for member in members:
        submissions_url = f"http://127.0.0.1:7777/view/submissions?contest={contest_name}&login={member}"
        submissions_response = requests.get(submissions_url)
        submissions_xml = submissions_response.text

        submissions_root = ET.fromstring(submissions_xml)
        submissions = submissions_root.findall('submission')

        solved_tasks = {}
        problem_tasks = {}
        for submission in submissions:
            verdict = submission.get('verdict')
            problem = submission.get('problem')
            timestamp = int(submission.get('timestamp'))

            if verdict == 'OK':
                if problem in solved_tasks:
                    if solved_tasks[problem] > timestamp:
                        solved_tasks[problem] = timestamp
                else:
                    solved_tasks[problem] = timestamp
            elif verdict == 'WA' or verdict == 'TL' or verdict == 'RE':
                if problem in problem_tasks:
                    problem_tasks[problem].append(timestamp)
                else:
                    problem_tasks[problem] = [timestamp]

        penalty = 0
        for item in problem_tasks:
            if item in solved_tasks:
                for penalty_time in problem_tasks[item]:
                    if penalty_time <= solved_tasks[item]:
                        penalty += 20
        
        for item in solved_tasks:
            penalty += solved_tasks[item]
        scores[member] = [len(solved_tasks), penalty]

    max_solutions = max(scores.values(), key=lambda x: (x[0], -x[1]))

    winners = []
    for member in scores:
        if scores[member] == max_solutions:
            winners.append(member)

    print(len(winners))
    for winner in sorted(winners):
        print(winner)


if __name__ == '__main__':
    main()

