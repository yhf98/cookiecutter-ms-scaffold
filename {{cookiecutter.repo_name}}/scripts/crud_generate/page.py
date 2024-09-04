from main import CrudGenerate

if __name__ == '__main__':
    '''
    Page CRUD
    '''
    from apps.models import Page
    crud = CrudGenerate(Page, "页面", "page")
    crud.generate_codes()
    crud.main()