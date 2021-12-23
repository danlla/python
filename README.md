SEED — симметричный блочный криптоалгоритм на основе Сети Фейстеля, разработанный Корейским агентством информационной безопасности (Korean Information Security Agency, KISA) в 1998 году.

В алгоритме используется 128-битный блок и ключ длиной 128 бит.
Алгоритм использует две 8 × 8 таблицы подстановки, которые выведены из дискретного возведения в степень (в этом случае, x247 и x251 — плюс некоторые «несовместимые операции»). 128-битовый полный шифр — сеть Фейстеля с F-функцией, воздействующей на 64-битовые половины, в то время как сама F-функция — Сеть Фейстеля, составленная из G-Функции, воздействующей на 32-разрядные половины. Однако рекурсия не простирается далее, потому что G-Функция — не Сеть Фейстеля. В G-Функции 32-разрядное слово рассматривают как четыре 8-битовых байта, каждый из которых проходит через одну или другую таблицу подстановки, затем объединяется в умеренно комплексном наборе булевых функций таким образом, что каждый бит вывода зависит от 3 из 4 входных байтов.
SEED имеет сложное ключевое расписание, генерируя тридцать два 32-разрядных дополнительных символа, используя G-Функции на сериях вращений исходного необработанного ключа, комбинированного со специальными раундовыми константами от «Золотого соотношения»

Алгоритм получил широкое распространение и используется финансовыми и банковскими структурами, производственными предприятиями и бюджетными учреждениями Южной Кореи.
SEED был принят несколькими стандартными протоколами: S / MIME ( RFC 4010 ), TLS / SSL (RFC 4162 ), IPSec (RFC 4196 ) и ISO / МЭК 18033-3:
А Ядро Linux поддерживает SEED с 2007 года.Википедия
