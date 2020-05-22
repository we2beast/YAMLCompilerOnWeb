from django.shortcuts import render


def index(request):
    # compiler.execute_compiler("./site_level_configuration_file.yaml", "./AUGMENTED_SITE_LEVEL_CONFIG_FILE.yaml", ".tmp")
    return render(request, 'index.html')
