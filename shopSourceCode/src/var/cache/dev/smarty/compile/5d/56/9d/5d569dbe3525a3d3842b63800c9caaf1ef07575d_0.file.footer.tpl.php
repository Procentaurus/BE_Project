<?php
/* Smarty version 3.1.48, created on 2023-11-26 15:18:56
  from '/var/www/html/pudaadmin/themes/new-theme/template/footer.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_656353d0922a81_89383986',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '5d569dbe3525a3d3842b63800c9caaf1ef07575d' => 
    array (
      0 => '/var/www/html/pudaadmin/themes/new-theme/template/footer.tpl',
      1 => 1701007189,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_656353d0922a81_89383986 (Smarty_Internal_Template $_smarty_tpl) {
?><div id="footer" class="bootstrap">
    <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['hook'][0], array( array('h'=>"displayBackOfficeFooter"),$_smarty_tpl ) );?>

</div>
<?php }
}
