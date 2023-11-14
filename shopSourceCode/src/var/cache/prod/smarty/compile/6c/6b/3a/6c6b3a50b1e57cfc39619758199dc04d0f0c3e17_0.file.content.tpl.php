<?php
/* Smarty version 3.1.48, created on 2023-11-08 20:03:56
  from '/var/www/html/pudaadmin/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_654bdb9c8a3a29_00417936',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '6c6b3a50b1e57cfc39619758199dc04d0f0c3e17' => 
    array (
      0 => '/var/www/html/pudaadmin/themes/default/template/content.tpl',
      1 => 1689769962,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_654bdb9c8a3a29_00417936 (Smarty_Internal_Template $_smarty_tpl) {
?><div id="ajax_confirmation" class="alert alert-success hide"></div>
<div id="ajaxBox" style="display:none"></div>

<div class="row">
	<div class="col-lg-12">
		<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
			<?php echo $_smarty_tpl->tpl_vars['content']->value;?>

		<?php }?>
	</div>
</div>
<?php }
}
