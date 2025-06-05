from django.contrib import admin
from .models import Author, Genre, Book, Language, BookInstance

class BookInline(admin.TabularInline):
    model = Book

@admin.register(Author)
# admin.site.register(Author, AuthorAdmin)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BookInline]
    

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
# admin.site.register(Book, BookAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre']
    
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
# admin.site.register(BookInstance, BookInstanceAdmin)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    list_display = ('book', 'status', 'due_back', 'id')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(BookInstance)


