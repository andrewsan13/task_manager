class Project:
    def __init__(self, p_id, name='None'):
        self.name: str = name
        self.p_id: int = p_id

    class Task:
        def __init__(self, t_id, project_id, name='Nothing', status='Closed', priority='Regular'):
            self.t_id: int = t_id
            self.name: str = name
            self.status: str = status
            self.project_id: int = project_id
            self.priority: str = priority
