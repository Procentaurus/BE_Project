<?php
/* Smarty version 3.1.48, created on 2023-11-26 15:18:56
  from '/var/www/html/pudaadmin/themes/new-theme/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_656353d08c3b96_49822110',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'b35e3d583b3bb5da8be4fbfc14f58ae627233473' => 
    array (
      0 => '/var/www/html/pudaadmin/themes/new-theme/template/content.tpl',
      1 => 1701007189,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_656353d08c3b96_49822110 (Smarty_Internal_Template $_smarty_tpl) {
?>
<div id="ajax_confirmation" class="alert alert-success" style="display: none;"></div>


<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
  <?php echo $_smarty_tpl->tpl_vars['content']->value;?>

<?php }
}
}
