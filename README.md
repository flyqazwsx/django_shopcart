## 如何上傳圖片與顯示圖片

- 在本地app models.py 新增一筆 image
    image = models.FileField(upload_to='image/', blank=True)
    # upload_to 指定上传文件位置
    # 这里指定存放在 img/ 目录下

- 在project settings.py 新增
    # 指定上传文件目录
    # replace() 将 "\\" 替换为 "/"
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace("\\", "/")

- 在app  views.py 新增

    - def create_shop(request):
        form = ProductForm()
        if request.method == 'POST':
            print('POST')
            if request.user.is_authenticated:
                form = ProductForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('view_shop')
        context = {
            'view_shop': view_shop,
            'form': form
        }

        return render(request, './shopcart/create_shop.html', context)


