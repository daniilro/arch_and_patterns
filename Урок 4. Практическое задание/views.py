'''

'''
from dindondon_framework.templator import renderer
from patterns.base_patterns import Engine  # , Logger

site = Engine()

TEMPLATES_FOLDER = 'templates'


#############################################################################
class PcWelcome:
    def __call__(self, request):
        return '200 OK', renderer(
            'contact.html', folder=TEMPLATES_FOLDER, data=request.get(
                'data', None))


#############################################################################
class PcIndex:
    def __call__(self, request):
        return '200 OK', renderer('index.html', objects_list=site.categories)


#############################################################################
class PcAbout:
    def __call__(self, request):
        return '200 OK', renderer(
            'about.html', folder=TEMPLATES_FOLDER, objects_list=site.categories)


#############################################################################
class PcInfo:
    def __call__(self, request):
        print(f"--- PcInfo ---")
        print(request)
        print(site.categories)
        return '200 OK', renderer(
            'info.html', folder=TEMPLATES_FOLDER, timestamp=request.get(
                'timestamp', None))


#############################################################################
class PcContact:
    def __call__(self, request):
        return '200 OK', renderer(
            'contact.html', folder=TEMPLATES_FOLDER, data=request.get(
                'data', None))


#############################################################################
class PcFeedback:
    def __call__(self, request):
        return '200 OK', renderer('feedback.html', folder=TEMPLATES_FOLDER)


#############################################################################
class PcCreateCategory:
    def __call__(self, request):

        print(request)

        if request['method'] == 'POST':
            print(request)
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category_id = data.get('category_id')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)

            site.categories.append(new_category)

            return '200 OK', renderer(
                'index.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', renderer(
                'create_category.html', folder=TEMPLATES_FOLDER, categories=categories)


#############################################################
class PcCoursesList:
    def __call__(self, request):
#        logger.log('Список курсов')
        try:
            category = site.find_category_by_id(int(request['request_params']['id']))
            return '200 OK', renderer('course_list.html', objects_list=category.courses, name=category.name, id=category.id)
        except KeyError:
            return '200 OK', 'No courses have been added yet'

#############################################################
class PcCreateCourse:
    category_id = -1

    def __call__(self, request):
        if request['method'] == 'POST':
            # метод пост
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                course = site.create_course('record', name, category)
                site.courses.append(course)

            return '200 OK', renderer('course_list.html', objects_list=category.courses,
                                    name=category.name, id=category.id)

        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', renderer('create_course.html', name=category.name, id=category.id)
            except KeyError:
                return '200 OK', 'No categories have been added yet'

#############################################################
class PcCopyCourse:
    def __call__(self, request):
        request_params = request['request_params']

        try:
            name = request_params['name']
            old_course = site.get_course(name)
            if old_course:
                new_name = f'copy_{name}'
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)

            return '200 OK', renderer('course_list.html', objects_list=site.courses)
        except KeyError:
            return '200 OK', 'No courses have been added yet'

#############################################################
pc_list = {
    '/': PcIndex(),  # PcWelcome(),
    '/index/': PcIndex(),
    '/about/': PcAbout(),
    '/info/': PcInfo(),
    '/feedback/': PcFeedback(),
    '/create-category/': PcCreateCategory(),
    '/courses-list/': PcCoursesList(),
    '/create-course/': PcCreateCourse(),
    '/copy-course/': PcCopyCourse()

}

#############################################################
