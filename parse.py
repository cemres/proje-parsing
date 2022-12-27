from resume_parser import resumeparse

data = resumeparse.read_file('cv.pdf')
print(data)