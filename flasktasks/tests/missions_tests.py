import unittest
from flasktasks import db
from flasktasks.tests.flasktasks_testcase import FlaskTasksTestCase
from flasktasks.models import Color, Tag, Category, Status


class CategorysTest(FlaskTasksTestCase):
    def setUp(self):
        super().setUp()
        self.valid_tag = Tag('valid tag', Color.BLUE)
        db.session.add(self.valid_tag)
        db.session.commit()

    def test_categories_page(self):
        first_category = Category('category a', 'description', self.valid_tag.id)
        second_category = Category('category b', 'description', self.valid_tag.id)
        db.session.add(first_category)
        db.session.add(second_category)
        db.session.commit()

        response = self.app.get('/categories')
        assert b'category a' in response.data
        assert b'category b' in response.data

    def test_new_category_form(self):
        response = self.app.get('/categories/new')
        assert b'New Category' in response.data

    def test_category_creation(self):
        data = { 'title':'some category', 'description':'a useful description',
                 'tag_id':self.valid_tag.id }
        response = self.app.post('/categories/new', data=data)
        assert response.status_code == 302

        response = self.app.get('/categories')
        assert b'some category' in response.data

if __name__ == '__main__':
    unittest.main()
