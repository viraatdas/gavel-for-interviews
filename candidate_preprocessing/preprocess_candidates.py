from collections import defaultdict
import pickle


def create_dictionary_of_candidates(pkl_file_dir):
    # begin = False
    # candidates_by_interviewers = defaultdict(dict)
    # candidate_name = None
    # interviewer_name = None
    # candidate_profile = ""
    # with open("all_candidates", "r") as f:
    #     for line in f.readlines():
    #         print(line)
    #         if "BEGIN" in line:
    #             begin = True
    #             continue
    #         elif "END" in line:

    #             if candidate_name and interviewer_name and candidate_profile:
    #                 candidates_by_interviewers[interviewer_name][candidate_name] = candidate_profile
    #             begin = False
    #             candidate_profile = ""
    #             continue
    #         if begin:
    #             if "Name:" in line:
    #                 candidate_name = line.split(": ")[1].rstrip()
    #                 candidate_name = candidate_name.replace(" ", "-")
    #                 continue
    #             elif "Interviewer name:" in line:
    #                 interviewer_name = line.split(": ")[1].rstrip()
    #                 continue
    #             else:
    #                 candidate_profile += line + "<br/>"
    # filehandler = open("candidate_profile.pkl", "wb")
    # pickle.dump(candidates_by_interviewers, filehandler)

    return pickle.load(open(pkl_file_dir, "rb"))





        