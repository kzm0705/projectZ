// HTMLから要素を取得
const menuIcon = document.getElementById('menu-icon');
const navMenu = document.getElementById('nav-menu');

// アイコンがクリックされたときの処理
menuIcon.addEventListener('click', function() {
    // 1. ナビゲーションメニューに 'open' クラスを付け外しする
    navMenu.classList.toggle('open');
    
    // 2. アイコン自体に 'change' クラスを付け外しし、X字にアニメーションさせる
    menuIcon.classList.toggle('change');
});