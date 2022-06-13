TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


    class Dialog:
        def __new__(cls, *args, **kwargs):
            if TYPE_OS == 1:
                obj = DialogWindows()
            else:
                obj = DialogLinux()
            setattr(obj, 'name', args[0])

            return obj

