def counts_remove(blacklist, files, query):
    deleted_files = {}

    for file in files:
        if file.startswith(query):
            if any(file.startswith(dir) for dir in blacklist):
                extension = '.' + file.split('.')[-1]
                deleted_files[extension] = deleted_files.get(extension, 0) + 1

    return deleted_files


def main():
    n = int(input())
    blacklist = [input() for _ in range(n)]

    m = int(input())
    files = [input() for _ in range(m)]

    q = int(input())
    queries = [input() for _ in range(q)]

    for query in queries:
        deleted_files = counts_remove(blacklist, files, query)

        print(len(deleted_files))
        for extension, counts in deleted_files.items():
            print(f'{extension}: {counts}')


if __name__ == '__main__':
    main()


