from gavel import app
from gavel.models import *
from gavel.constants import *
import gavel.settings as settings
import gavel.utils as utils
import gavel.stats as stats
from flask import (
    redirect,
    render_template,
    request,
    url_for,
)
import urllib.parse
import xlrd
from candidate_preprocessing.preprocess_candidates import create_dictionary_of_candidates

import os
@app.route('/<interviewer_name>/<candidate>')
def render_candidate(interviewer_name, candidate):
    candidates_by_interviewers = create_dictionary_of_candidates()
    return candidates_by_interviewers[interviewer_name][candidate]
    # return render_template("candidate.html", interviewer_name=interviewer_name, candidate=candidate)
