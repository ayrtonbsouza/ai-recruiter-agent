from tinydb import TinyDB, Query

class AnalyzeDatabase(TinyDB):
  def __init__(self, database_path='db.json'):
    super().__init__(database_path)
    self.jobs = self.table('jobs')
    self.resumes = self.table('resumes')
    self.analysis = self.table('analysis')
    self.files = self.table('files')

  def get_job_by_name(self, name):
    job = Query()
    results = self.jobs.search(job.name == name)
    return results[0] if results else None

  def get_resume_by_id(self, id):
    resume = Query()
    results = self.resumes.search(resume.id == id)
    return results[0] if results else None

  def get_analysis_by_job_id(self, job_id):
    analysis = Query()
    results = self.analysis.search(analysis.job_id == job_id)
    return results
  
  def get_resumes_by_job_id(self, job_id):
    resume = Query()
    results = self.resumes.search(resume.job_id == job_id)
    return results
