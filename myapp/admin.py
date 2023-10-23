from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import shoes,users
from django.contrib import admin
from django.core.files.images import ImageFile
from django import forms
import glob
import os
from django.core.files.uploadedfile import UploadedFile


class YourModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Perform any additional processing before saving the model
        if change:
            # The model instance is being edited
            previous_name = shoes.objects.get(pk=obj.pk).name
        
        # Access the uploaded file
        uploaded_file = form.cleaned_data['image']
        
        def get_image_files(directory):
            image_files = glob.glob(os.path.join(directory, '*.*'))
            image_files = [ImageFile(open(file, 'rb'), name=os.path.basename(file)) for file in image_files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif',".jfif"))]
            return image_files
        existing_files=get_image_files("media/")
        count=1
        for image in existing_files:
            image_name=image.name
            original_name = image_name.rsplit('.', 1)[0]
            upload_name=uploaded_file.name
            new_name = upload_name.rsplit('.', 1)[0]
            print(original_name)
            print(new_name)
            if original_name==new_name:
                print("There is a similar file")
                app_label = self.model._meta.app_label
                model_name = self.model._meta.model_name
                changelist_url = reverse('admin:{0}_{1}_changelist'.format(app_label, model_name))
                return HttpResponseRedirect(changelist_url)
        # Call the superclass's save_model method to perform the default saving
            elif original_name!=new_name and len(existing_files)==count:
                super().save_model(request, obj, form, change)
                print("Saved Succesfully")
            count=count+1
admin.site.register(shoes, YourModelAdmin)
admin.site.register(users)



# Register your models here.
