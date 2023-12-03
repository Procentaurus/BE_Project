<?php
/* Smarty version 3.1.48, created on 2023-11-26 15:40:15
  from '/var/www/html/admintokar/themes/new-theme/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_656358cfa659c0_63334714',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '0aff272c4ea67e5fa07aa2cc2588c0fbc5f2d7a8' => 
    array (
      0 => '/var/www/html/admintokar/themes/new-theme/template/content.tpl',
      1 => 1689769962,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_656358cfa659c0_63334714 (Smarty_Internal_Template $_smarty_tpl) {
?>
<div id="ajax_confirmation" class="alert alert-success" style="display: none;"></div>


<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
  <?php echo $_smarty_tpl->tpl_vars['content']->value;?>

<?php }
}
}
