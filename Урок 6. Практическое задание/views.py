'''

'''

from dindondon_framework.templator import renderer
from patterns.base_patterns import Engine, Logger
from patterns.behavers import ListView, CreateView
from patterns.decors import AppRouter, TimeIt

site = Engine()
logger = Logger('main')

pc_list = {}

TEMPLATES_FOLDER = 'templates'


#############################################################################
class PcWelcome:
    def __call__(self, request):
        logger.log("PcWelcome.__call__")
        return '200 OK', renderer(
            'contact.html', folder=TEMPLATES_FOLDER, data=request.get(
                'data', None))


#############################################################################
@AppRouter(routes=pc_list, url='/')
class PcIndex:
    @TimeIt(name="PcIndex")
    def __call__(self, request):
        logger.log(f"{self.__class__.__name__} calling. request = {request}")
        return '200 OK', renderer('index.html', objects_list=site.categories)


#############################################################################
@AppRouter(routes=pc_list, url='/about/')
class PcAbout:
    @TimeIt(name="PcAbout")
    def __call__(self, request):
        return '200 OK', renderer(
            'about.html', folder=TEMPLATES_FOLDER, objects_list=site.categories)


#############################################################################
@AppRouter(routes=pc_list, url='/info/')
class PcInfo:
    @TimeIt(name="PcInfo")
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
@AppRouter(routes=pc_list, url='/feedback/')
class PcFeedback:
    @TimeIt(name="PcFeedback")
    def __call__(self, request):
        return '200 OK', renderer('feedback.html', folder=TEMPLATES_FOLDER)


#############################################################################
@AppRouter(routes=pc_list, url='/create-category/')
class PcCreateCategory:
    @TimeIt(name="PcCreateCategory")
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
@AppRouter(routes=pc_list, url='/courses-list/')
class PcCoursesList:
    @TimeIt(name="PcCoursesList")
    def __call__(self, request):
        logger.log('Список курсов')
        try:
            category = site.find_category_by_id(
                int(request['request_params']['id']))
            return '200 OK', renderer(
                'course_list.html', objects_list=category.courses, name=category.name, id=category.id)
        except KeyError:
            return '200 OK', 'No courses have been added yet'


#############################################################
@AppRouter(routes=pc_list, url='/create-course/')
class PcCreateCourse:
    category_id = -1

    @TimeIt(name="PcCreateCourse")
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
                print(request['request_params'])
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', renderer(
                    'create_course.html', name=category.name, id=category.id)
            except KeyError:
                return '200 OK', 'No categories have been added yet'


#############################################################
@AppRouter(routes=pc_list, url='/copy-course/')
class PcCopyCourse:
    @TimeIt(name="PcCopyCourse")
    def __call__(self, request):

        print(f"PcCopyCourse - request: {request}")

        request_params = request['request_params']

        try:
            name = request_params['name']
            old_course = site.get_course(name)
            if old_course:
                new_name = f'copy_{name}'
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)

            return '200 OK', renderer(
                'course_list.html', objects_list=site.courses)
        except KeyError:
            return '200 OK', 'No courses have been added yet'


#############################################################

@AppRouter(routes=pc_list, url='/student-list/')
class StudentListView(ListView):
    queryset = site.students
    template_name = 'student_list.html'


#############################################################
@AppRouter(routes=pc_list, url='/create-student/')
class StudentCreateView(CreateView):
    template_name = 'create_student.html'

    def create_obj(self, data: dict):
        name = data['name']
        name = site.decode_value(name)
        new_obj = site.create_user('student', name)
        site.students.append(new_obj)


#############################################################
@AppRouter(routes=pc_list, url='/add-student/')
class AddStudentByCourseCreateView(CreateView):
    template_name = 'add_student.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['courses'] = site.courses
        context['students'] = site.students
        return context

    def create_obj(self, data: dict):
        course_name = data['course_name']
        course_name = site.decode_value(course_name)
        course = site.get_course(course_name)
        student_name = data['student_name']
        student_name = site.decode_value(student_name)
        student = site.get_student(student_name)
        course.add_student(student)

#############################################################
