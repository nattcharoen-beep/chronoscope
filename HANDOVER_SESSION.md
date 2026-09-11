# 📋 CHRONOSCOPE: เอกสารส่งต่องานสำหรับเริ่มห้องแชทใหม่ (Project Handover Document)

> **บันทึกล่าสุด:** กันยายน 2026  
> **เวอร์ชันปัจจุบัน:** **v7.5** (Default Home & Brand Logo Navigation + 100% Feature Parity)  
> **สถานะ Git:** กิ่ง `main` และ `gh-pages` สะอาด ซิงค์ตรงกับรีโมต GitHub 100%  

---

## 1. ข้อมูลพื้นฐานโครงการ (Project Overview)
- **ชื่อโครงการ:** **CHRONOSCOPE: A Brief History of Us** (9 ยุค ส่องโลกผ่านม้วนฟิล์มและวรรณกรรม)
- **เป้าหมาย:** สื่อการเรียนการสอนประวัติศาสตร์สากลเชิงวิชาการระดับอุดมศึกษา บูรณาการ 9 มหายุค เข้ากับภาพยนตร์ 56 เรื่อง, วรรณกรรม 45 เล่ม, บทความวิจัย 38 บทความ, แผนที่ภูมิรัฐศาสตร์ 39 จุดยุทธศาสตร์, คลังมายาคติ 45 เรื่อง และระบบควิซประเมินผล 50 ข้อ
- **พาธโฟลเดอร์เครื่อง:** `C:\Users\nattc\OneDrive\Desktop\AI ลองไปเรื่อย\A brief history of us`
- **GitHub Repository:** `https://github.com/nattcharoen-beep/chronoscope.git`
- **Live GitHub Pages URL:**
  - 🇹🇭 **ฉบับภาษาไทย:** `https://nattcharoen-beep.github.io/chronoscope/index.html`
  - 🇬🇧 **ฉบับภาษาอังกฤษ:** `https://nattcharoen-beep.github.io/chronoscope/index_en.html`

---

## 2. สถานะล่าสุดของระบบ (Current System State - v7.5)

### ✅ สิ่งที่ทำสำเร็จสมบูรณ์แล้ว 100%:
1. **Default Home Screen (หน้าเริ่มต้นของเว็บ):**
   - เมื่อเปิดเข้าเว็บครั้งแรกไม่ว่าจะภาษาไทยหรืออังกฤษ (`/`, `index.html`, `index_en.html`) ระบบจะนำทางเข้าสู่ **Slide 0 (Title / Hero Cover)** เสมอ
   - ปรับฟังก์ชัน `restoreNavState()` ให้ตรวจจับหากไม่มี URL hash จะเรียกใช้ `goToDefaultHome()`
   - รองรับ `#home`, `#default`, `#slides` และ `#slide-0` ชี้ตรงไปยังหน้าปก
2. **Top-Left Brand Logo Navigation (คลิกโลโก้ CHRONOSCOPE บนซ้าย):**
   - มีฟังก์ชัน `goToDefaultHome()` ปิดทุกโมดอลที่เปิดค้างอยู่ นำทางกลับ `view-slides`, รีเซ็ตไปที่ Slide 0 (01 / 20), เลื่อนหน้าจอขึ้นบนสุดอย่างนุ่มนวล และปรับ hash เป็น `#slide-0` ทำงานตรงกันทั้งไทยและอังกฤษ
3. **100% Feature Parity ระหว่างไทยและอังกฤษ (v7.4):**
   - แผนที่ภูมิรัฐศาสตร์โลก (`#view-map`) แสดงผลแบบ Widescreen `max-w-[1700px]` เต็มจอทั้งสองภาษา
   - พิกัดยุทธศาสตร์ครบ 39 พิกัด (`world_overview` รวมอยู่ด้วย)
   - แท็บเมนูนำทางหลัก 8 แท็บตรงกัน 1:1:
     1. สไลด์บรรยาย (`#tab-slides`)
     2. ไทม์ไลน์ 9 ยุค (`#tab-timeline`)
     3. ผังมโนทัศน์ / เมโทร (`#tab-mindmap`)
     4. คลังบทความวิจัย (`#tab-articles`)
     5. คลังภาพยนตร์ประวัติศาสตร์ (`#tab-movies`)
     6. คลังวรรณกรรมคลาสสิก (`#tab-literature`)
     7. แผนที่ภูมิรัฐศาสตร์โลก (`#tab-map`)
     8. ข้อสอบวัดผล 10 ข้อ / สลับ 5 ชุด (`#tab-quiz`)
   - ระบบแบบทดสอบภาษาอังกฤษ (`history_quiz_sets_en.json`) ครบ 5 ชุด 50 ข้อ พร้อม Bloom's Taxonomy, ระดับความยาก, คำอธิบายเฉลยวิชาการ และการวิเคราะห์ตัวเลือกหลอก A, B, C, D
   - ปุ่ม `🗺️ Geopolitical Map` บนหัวสไลด์ภาพรวม 9 ยุคครบถ้วน
   - ผังสไลด์ (`⊞ Slide Grid`) บนแถบควบคุมด้านล่าง และกดตัวนับสไลด์เพื่อเปิดผังได้
   - ระบบบุ๊กมาร์ก (Bookmarks) มีคอนโทรลเลอร์ทำงานสมบูรณ์ทั้งสองภาษา
4. **การรักษาสถานะข้ามภาษา (Cross-Language State Preservation - v7.3):**
   - กดสลับภาษา TH ⇄ EN ไม่เด้งกลับหน้าแรก ระบบจะจดจำหน้าสไลด์, แท็บที่เลือก, หรือโมดอลที่เปิดอยู่ไปแสดงผลในอีกภาษาทันที
5. **การทดสอบและการ Deploy:**
   - ตรวจสอบโครงสร้าง HTML และ Syntax JavaScript ผ่าน 100% ไม่มี syntax errors
   - ซิงค์กิ่ง `main` และ `gh-pages` บน GitHub Actions ล่าสุดสำเร็จแล้ว

---

## 3. กฎเหล็กในการพัฒนา (Development Rules & Guidelines)
เมื่อรับช่วงต่อในห้องแชทใหม่ กรุณาปฏิบัติตามหลักการต่อไปนี้อย่างเคร่งครัด:
1. **ยึดภาษาไทย (`index.html`) เป็น Master Reference:** ทุกครั้งที่มีการแก้ไของค์ประกอบ โครงสร้าง หรือฟังก์ชัน ต้องอัปเดตให้ `index_en.html` เท่าเทียมกันแบบ 1:1 เสมอ
2. **รักษาความสมบูรณ์ของโครงสร้างสไลด์:** หน้าสไลด์ทั้ง 20 สไลด์ (`.slide-item`, 0 ถึง 19) ต้องเปิดและปิดแท็ก `</div>` ถูกต้องเสมอ ไม่ให้เกิด layout cascade overflow
3. **การจัดการข้อความและบรรทัด (CRLF / Encoding):** ไฟล์ในโปรเจกต์นี้ใช้ UTF-8 และ Windows CRLF (`\r\n`) ในการแก้ไขด้วยสคริปต์ Node.js ต้องระวังการแทนที่ regex ให้คำนึงถึงบรรทัดใหม่
4. **ขั้นตอนการ Deploy ขึ้น GitHub Pages:**
   ```bash
   git add .
   git commit -m "feat/fix: <รายละเอียดงาน>"
   git push origin main
   git checkout gh-pages
   git merge main --no-edit
   git push origin gh-pages
   git checkout main
   ```

---

## 4. ไฟล์สำคัญในโปรเจกต์ (Core Project Files)
- `index.html`: เว็บไซต์หลักฉบับภาษาไทย (Master)
- `index_en.html`: เว็บไซต์หลักฉบับภาษาอังกฤษ (1:1 Parity)
- `CHANGELOG.md`: บันทึกประวัติการพัฒนาตั้งแต่ v1.0 ถึง v7.5
- `history_database.json`: ฐานข้อมูลประวัติศาสตร์และเหตุการณ์สำคัญ 9 ยุค
- `deep_dive_articles.json` & `deep_dive_articles_en.json`: บทความวิชาการเชิงลึก
- `history_movies.json` & `history_movies_en.json`: ข้อมูลภาพยนตร์ 56 เรื่อง
- `history_literature.json` & `history_literature_en.json`: ข้อมูลวรรณกรรม 45 เล่ม
- `history_quiz_sets.json` & `history_quiz_sets_en.json`: ชุดข้อสอบ 5 ชุด (50 ข้อ)
- `history_glossary.json`: อภิธานศัพท์ประวัติศาสตร์ 2 ภาษา

---

## 5. ข้อความ Prompt สำหรับคัดลอกไปวางในห้องแชทใหม่ (Ready-to-Paste Prompt)

```markdown
สวัสดีครับ! เรามาทำงานต่อเนื่องในโปรเจกต์ "CHRONOSCOPE: A Brief History of Us" (มหากาพย์ประวัติศาสตร์โลก & ภาพยนตร์ประกอบการสอนสำหรับระดับอุดมศึกษา)

📁 ที่อยู่โปรเจกต์ในเครื่อง:
C:\Users\nattc\OneDrive\Desktop\AI ลองไปเรื่อย\A brief history of us

🌐 ลิงก์ออนไลน์ (GitHub Pages):
- ไทย: https://nattcharoen-beep.github.io/chronoscope/index.html
- อังกฤษ: https://nattcharoen-beep.github.io/chronoscope/index_en.html
- รีโป: https://github.com/nattcharoen-beep/chronoscope.git

📌 สถานะปัจจุบันของระบบ (เวอร์ชันล่าสุด v7.5):
1. กิ่ง main และ gh-pages สะอาดและซิงค์ล่าสุดเรียบร้อย (commit 1f407d1)
2. หน้าเริ่มต้น (Default Home) กำหนดให้เปิดเข้าที่ Slide 0 (หน้าปกหลักสูตร) เสมอทั้งไทยและอังกฤษ
3. โลโก้แบรนด์ CHRONOSCOPE ด้านบนซ้าย ผูกฟังก์ชัน goToDefaultHome() ไว้แล้ว (ปิดทุกโมดอล, สลับไป view-slides, กลับ Slide 0, เลื่อนขึ้นบนสุด และตั้ง hash #slide-0)
4. ทั้งสองภาษา (index.html และ index_en.html) มี Feature Parity ครบ 1:1 ทั้ง 8 แท็บเมนู, แผนที่ Widescreen 1700px (39 พิกัด), ระบบควิซ 5 ชุด 50 ข้อ, ผังสไลด์ และระบบบุ๊กมาร์ก
5. รายละเอียดประวัติการพัฒนาทั้งหมดบันทึกไว้ใน CHANGELOG.md

⚖️ กฎเหล็กในการทำงาน:
- ยึด index.html (ภาษาไทย) เป็นมาตรฐานหลักเสมอ ทุกครั้งที่มีการแก้ UI หรือฟังก์ชัน ต้องอัปเดต index_en.html ให้ตรงกันแบบ 1:1
- โครงสร้างสไลด์ต้องครบ 20 สไลด์ (.slide-item 0-19) พร้อมแท็กปิดสมบูรณ์
- เมื่อเสร็จงาน ต้องทดสอบ syntax และ push ขึ้นทั้งกิ่ง main และ merge เข้า gh-pages เพื่อให้ GitHub Pages อัปเดตเสมอ

กรุณาตรวจสอบ git status และสถานะโปรเจกต์ เพื่อเตรียมพร้อมรับคำสั่งต่อไปได้เลยครับ!
```
