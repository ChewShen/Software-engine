from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError
from AllUsers.models import CustomUser

class Command(createsuperuser.Command):
    help = 'Create a superuser with the role "admin"'

    def handle(self, *args, **options):
        try:
            # print("Options:", options)  # Add this line for debugging
            
            # Call the original createsuperuser command
            super().handle(*args, **options)
            
            # Get the created superuser
            username = options['username']
            superuser = CustomUser.objects.get(username=username)

            # Assign role "admin" to the superuser
            superuser.role = 'Admin'
            superuser.save()
            
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully with role "Admin"'))
        except CustomUser.DoesNotExist:
            raise CommandError(f"CustomUser matching query does not exist for username: {username}")
        except Exception as e:
            raise CommandError(f"Error creating superuser: {e}")
