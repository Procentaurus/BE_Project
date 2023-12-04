<?php
/* Smarty version 3.1.48, created on 2023-11-26 16:19:41
  from '/var/www/html/admintokar/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_6563620dbd4468_11687933',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'c2be4671df501bd5808b7f3b0072bc7e3a662e66' => 
    array (
      0 => '/var/www/html/admintokar/themes/default/template/content.tpl',
      1 => 1689769962,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6563620dbd4468_11687933 (Smarty_Internal_Template $_smarty_tpl) {
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
