using System;

namespace gg
{
    class gg {         
        public static void RemoveMissingScripts(project_rabota go)
{
   int count = project_rabotaUtility.GetMonoBehavioursWithMissingScriptCount(go);
   if (count > 0)
   {
       // Edit: use undo record object, since undo destroy wont work with missing
       Undo.RegisterCompleteObjectUndo(go, "Remove missing scripts");
       project_rabotaUtility.RemoveMonoBehavioursWithMissingScript(go);
   }
   foreach (Transform childT in go.transform)
   {
       RemoveMissingScripts(childT.project_rabota);
   }
}
    }
}