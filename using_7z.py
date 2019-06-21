import os
import patoolib


class extract_using_7z:
    def __init__(self):
        self.basepath = "E:/Courses Drive/"
        self.outpath = "D:/ELITE Club/"

    def _find_first_file(self, dir_lst):
        file_size = []
        first_file = None
        if len(dir_lst) == 1:
            return dir_lst[0]
        else:
            for d in dir_lst:
                self._file_path = os.path.join(self._dir_path, d)
                extension = d.split(".")
                last = extension[-2]
                if extension[-2] == 'part1' or extension[-2] == 'part01':
                    # This will return file with contain part1
                    first_file = d
                    break
                elif extension[-1] == 'ini':
                    # This will remove file with extension .ini
                    try:
                        os.remove(self._file_path)
                    except Exception as e:
                        print(e)

                elif len(extension[-2]) > 6:
                    # Give file name is minimum length
                    file_size.append(os.path.getsize(self._file_path))
                    if len(file_size) == 0:
                        pass
                    else:
                        minimum_length = max(file_size)
                        first_file = dir_lst[file_size.index(minimum_length)]

        return first_file


    def multi_file(self):

        # f = open(self.outpath + '/fileList.txt', "w")  # 'r' for reading and 'w' for writing
        for entry in os.listdir(self.basepath):
            self._dir_path = os.path.join(self.basepath, entry)
            if os.path.isdir(self._dir_path):
                dir_file_list = os.listdir(self._dir_path)
                self._first_file = self._find_first_file(dir_file_list)

                first_file_path = self._dir_path + '/' + self._first_file

                # f.write(first_file_path + ',')  # Write inside file

                try:
                    patoolib.extract_archive(first_file_path, pwd="@FTUCHAT", outdir=self.outpath)
                except Exception as e:
                    print('File: {} Error: {}'.format(self._first_file, e))
                    print(e)
                # f.close()


class match_dir:
    def __init__(self):
        self.mainpath = "D:/Users/Sachin/Google Drive/Study/Stock/ELITE CLUB/101-200 Courses FTU ELITE/"
        self.basepath = "E:/Courses Drive/"
        self.main_files_lst = [x for x in os.listdir(self.mainpath)]
        self.base_files_lst = [x for x in os.listdir(self.basepath)]

    def match_size(self):
        counter = 0
        for i in self.main_files_lst:
            b_file = self.base_files_lst[counter]
            m_file_path = os.path.join(self.mainpath, i)
            b_file_path = os.path.join(self.basepath, b_file)
            if os.path.getsize(m_file_path) == os.path.getsize(b_file_path):
                print("True: ", b_file)
            else:
                print('False: ', b_file)

            counter = counter + 1

    def del_rar(self):
        counter = 0
        try:
            for i in self.main_files_lst:
                subpath = os.path.join(self.mainpath, i)
                sub_files_lst = [x for x in os.listdir(subpath)]
                if os.path.isdir(subpath):
                    for s in sub_files_lst:
                        file_path = os.path.join(subpath, s)
                        filename, file_extension = os.path.split(file_path)

                        extension = s.split(".")[-1]

                        if extension == 'rar' or extension == 'ini':
                            os.remove(file_path)
                            counter = counter + 1
                else:
                    print(False)
                    main_file_path = os.path.join(self.mainpath, i)
                    extension = i.split(".")[-1]
                    if extension == 'rar' or extension == 'ini':
                        os.remove(main_file_path)
                        counter = counter + 1



                    # print('filename: {} \n extancen {}'.format(filename, exename))
        except NotADirectoryError as e:
            print(e)

        print('\nCounter: ', counter)

    def match_name(self):
        counter = 0
        for i in self.main_files_lst:
            b_file = self.base_files_lst[counter]
            print(os.path.join(self.mainpath, i))
            if i == b_file:
                pass
            else:
                diff = []
                for s in range(len(i)):
                    if i[s] == b_file[s]:
                        pass
                    else:
                        diff.append(i[s])
                print('False: {} -- {}'.format(i, diff))
            counter = counter + 1


if __name__ == '__main__' :
    f = extract_using_7z()
    f.multi_file()