<?php
/* Smarty version 3.1.48, created on 2023-11-14 17:36:02
  from '/var/www/html/pudaadmin/themes/new-theme/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_6553a1f269a005_89684112',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'b35e3d583b3bb5da8be4fbfc14f58ae627233473' => 
    array (
      0 => '/var/www/html/pudaadmin/themes/new-theme/template/content.tpl',
      1 => 1699558336,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6553a1f269a005_89684112 (Smarty_Internal_Template $_smarty_tpl) {
?>
<div id="ajax_confirmation" class="alert alert-success" style="display: none;"></div>


<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
  <?php echo $_smarty_tpl->tpl_vars['content']->value;?>

<?php }
}
}
