        // 禁用右键菜单
        document.addEventListener('contextmenu', function (e) {
            e.preventDefault();
            alert('右键菜单已禁用');
        });

        // 禁用F12键
        document.addEventListener('keydown', function (e) {
            if (e.key === 'F12') {
                e.preventDefault();
                alert('F12已禁用');
            }
        });

        // 禁用复制和粘贴
        document.addEventListener('copy', function (e) {
            e.preventDefault();
            alert('复制粘贴功能已禁用');
        });

        document.addEventListener('paste', function (e) {
            e.preventDefault();
            alert('复制粘贴功能已禁用');
        });


        