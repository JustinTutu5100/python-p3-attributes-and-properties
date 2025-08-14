class Person:
    approved_jobs = ["Sales", "Engineer", "Manager", "Chef", "ITC"]

    def __init__(self, name=None, job=None):
        if name is not None:
            if isinstance(name, str) and 1 <= len(name) <= 25:
                self.name = name.title()
            else:
                print("Name must be string between 1 and 25 characters.")
                self.name = None
        else:
            self.name = None

        if job is not None:
            if job in self.approved_jobs:
                self.job = job
            else:
                print("Job must be in list of approved jobs.")
                self.job = None
        else:
            self.job = None
