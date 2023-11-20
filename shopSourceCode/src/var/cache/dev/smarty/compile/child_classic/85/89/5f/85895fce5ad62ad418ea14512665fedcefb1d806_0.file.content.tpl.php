<?php
/* Smarty version 3.1.48, created on 2023-11-20 21:27:52
  from '/var/www/html/modules/blockreassurance/views/templates/admin/tabs/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_655bc1485673e8_92619135',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '85895fce5ad62ad418ea14512665fedcefb1d806' => 
    array (
      0 => '/var/www/html/modules/blockreassurance/views/templates/admin/tabs/content.tpl',
      1 => 1700427565,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
    'file:./content/listing.tpl' => 1,
    'file:./content/config.tpl' => 1,
  ),
),false)) {
function content_655bc1485673e8_92619135 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_subTemplateRender("file:./content/listing.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>

<?php $_smarty_tpl->_subTemplateRender("file:./content/config.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
}
}
