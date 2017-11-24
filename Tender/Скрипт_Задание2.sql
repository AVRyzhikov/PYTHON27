/* Предварительно */
/* удаляем рабочую таблицу */
drop  table if exists all_ef;

/****************************************************************
*** формируем  рабочую таблицу  с ээфективностями всех  дизайнов из статистики *** */
create table all_ef
 (
  select sdc.site_area_id Блок_ID, sdc.design_id Дизайн_ID, sum(sdc.partner_gain)/sum(sdc.view_count)*1000  Эффективность from stat_design_cache sdc
   /*where sdc.design_id <> 0 */
   group by sdc.site_area_id, sdc.design_id
 );
/****************************************************************/


select user.user_id Вебмастер_ID, site.site_id Сайт_ID,site_area_id Блок_ID,site_area.name Имя_блока, best_d.Дизайн_ID Дизайн_ID, best_d.Имя_дизайна  Имя_дизайна,
best_d.Эффективность from  user, site, site_area,

( 
  select site_area_id Блок_ID, min(site_area_design_1_id) Дизайн_ID,  name Имя_дизайна,res.Эффективность  from 
 ( 
  select  *  from site_area_design_1 sad
     left join /* дополняем "плохими" дизайнами, если в  блоке все дизайны "плохие", выбираем миинимальный ID.  */ 
   ( 
    select all_ef.Блок_ID, min(all_ef.Дизайн_ID) Дизайн_ID, all_ef.Эффективность  from all_ef,
     (
      select  Блок_ID Блок_ID,  max(Эффективность) Эффективность from all_ef 
      group by Блок_ID
     ) t1 
     where all_ef.Блок_ID=t1.Блок_ID  and all_ef.Эффективность= t1.Эффективность
     group by all_ef.Блок_ID,all_ef.Эффективность 
   ) max_ef /* максимальные  эффективности дизайнов */
  on sad.site_area_id=max_ef.Блок_ID 
  where  sad.site_area_id=max_ef.Блок_ID and  sad.site_area_design_1_id=max_ef.Дизайн_ID or 
  Блок_id is NULL
  ) res
  
 group by Блок_ID 
 ) best_d
 
 where user.user_id=site.user_id and site.site_id=site_area.parent_id and site_area.site_area_id=best_d.Блок_ID
 
 order by  Вебмастер_ID,  Сайт_ID, Блок_ID;
 
 /* удаляем рабочую таблицу */
drop  table if exists all_ef;
 