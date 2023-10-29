from .models import Project
from table import Table
from table.columns import Column

class ProjectTable(Table):
  id = Column(field='id')
  name = Column(field='name')
  submission_date = Column(field='submission_date')
  class Meta:
     model = Project