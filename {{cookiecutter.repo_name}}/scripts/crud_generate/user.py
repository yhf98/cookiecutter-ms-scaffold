from main import CrudGenerate

if __name__ == '__main__':
    '''
    Page CRUD
    '''
    from apps.models import User
    crud = CrudGenerate(User, "用户", "user")
    crud.generate_codes()
    crud.main()