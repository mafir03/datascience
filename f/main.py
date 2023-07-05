import utils


def main():
    arr = utils.fileList("rsc")
    for item in arr:
        x = utils.readCsv("rsc/" + item)
        print(x.head())

if __name__ == '__main__':
    main()
