const totalDays = 24;
const currentDay = new Date().getDate(); 

const grid = document.getElementById('calendar-grid');
const modal = document.getElementById('modal-overlay');
const closeBtn = document.getElementById('close-btn');
const animWrapper = document.getElementById('css-anim-wrapper');

function initCalendar() {
    const dateEl = document.getElementById('current-date');
    if(dateEl) dateEl.innerText = `Bugün: ${new Date().toLocaleDateString('tr-TR')}`;
    
    createSnowflakes();

    const openedBoxes = getOpenedBoxes();
    for (let i = 1; i <= totalDays; i++) {
        createBox(i, openedBoxes.includes(i));
    }
}

function createSnowflakes() {
    const snowflakeCount = 50;
    const body = document.body;
    
    for (let i = 0; i < snowflakeCount; i++) {
        const snow = document.createElement('div');
        snow.innerHTML = '❄';
        snow.classList.add('snowflake');
        
        snow.style.left = Math.random() * 100 + 'vw';
        snow.style.animationDuration = Math.random() * 3 + 5 + 's'; 
        snow.style.animationDelay = Math.random() * 5 + 's'; 
        snow.style.opacity = Math.random() * 0.5 + 0.3;
        snow.style.fontSize = Math.random() * 10 + 10 + 'px';
        
        body.appendChild(snow);
    }
}

function getOpenedBoxes() {
    const stored = localStorage.getItem('openedBoxes');
    return stored ? JSON.parse(stored) : [];
}

function saveOpenedBox(dayNum) {
    const opened = getOpenedBoxes();
    if (!opened.includes(dayNum)) {
        opened.push(dayNum);
        localStorage.setItem('openedBoxes', JSON.stringify(opened));
    }
}

function createBox(dayNum, isOpened) {
    const box = document.createElement('div');
    box.classList.add('box');
    
    if (dayNum === currentDay) {
        box.classList.add('current-day');
    }

    if (isOpened) {
        box.classList.add('opened');
        box.innerHTML = `✅ <br><span style="font-size:14px">${dayNum}</span>`;
        box.onclick = () => openModal(dayNum, true); 
    } else if (dayNum > currentDay) {
        box.classList.add('locked');
        box.innerHTML = `🔒 <br><span style="font-size:14px">${dayNum}</span>`;
        box.onclick = () => {
            box.classList.add('shake-anim');
            setTimeout(() => box.classList.remove('shake-anim'), 500);
            alert(`Sabırsızlanma! ${dayNum} Aralık'ı beklemen lazım.`);
        };
    } else {
        box.classList.add('unlocked');
        box.innerHTML = `${dayNum}`;
        box.onclick = () => openModal(dayNum, false);
    }
    grid.appendChild(box);
}

async function openModal(dayNum, alreadyOpened) {
    modal.classList.remove('hidden');
    
    document.getElementById('modal-title').innerText = `${dayNum} Aralık`;
    const descArea = document.getElementById('modal-desc');
    descArea.innerText = "Lavix düşünüyor...";
    
    animWrapper.innerHTML = '';
    animWrapper.className = ''; 

    try {
        confetti({ particleCount: 150, spread: 80, origin: { y: 0.6 }, zIndex: 9999 });
    } catch (e) {}

    if (alreadyOpened) {
        descArea.innerText = "Bu kutuyu zaten açtın! İşte ödülün:";
        playCssAnim("✅", "party-pop"); 
        return;
    }

    try {
        // NOT: Canlıya alırken buradaki localhost adresi değişecek.
        const response = await fetch(`/reward/${dayNum}`);
        if (!response.ok) throw new Error("API Hatası");
        
        const data = await response.json();
        
        descArea.innerText = data.content;
        playCssAnim(data.icon, data.effect);

        saveOpenedBox(dayNum);
        
        const boxElement = grid.children[dayNum - 1];
        if (boxElement) {
            boxElement.classList.remove('unlocked');
            boxElement.classList.add('opened');
            boxElement.innerHTML = `✅ <br><span style="font-size:14px">${dayNum}</span>`;
            boxElement.onclick = () => openModal(dayNum, true);
        }
    } catch (error) {
        console.error(error);
        descArea.innerText = "Bağlantı hatası. Lütfen daha sonra tekrar deneyin.";
    }
}

function playCssAnim(icon, effectClass) {
    animWrapper.innerHTML = `<span>${icon}</span>`;
    animWrapper.children[0].classList.add(effectClass);
}

closeBtn.onclick = () => {
    modal.classList.add('hidden');
};

function resetCalendar() {
    if(confirm("Tüm ilerlemeniz silinecek. Emin misiniz?")) {
        localStorage.clear();
        location.reload();
    }
}

initCalendar();